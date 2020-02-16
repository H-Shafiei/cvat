import React from 'react';

import { connect } from 'react-redux';
import { CombinedState } from "../../reducers/interfaces";

import {
    Row,
    Col,
    Button,
    Dropdown,
    Icon,
} from 'antd';

import Text from 'antd/lib/typography/Text';

import ActionsMenuContainer from '../../containers/actions-menu/actions-menu';
import { MenuIcon } from '../../icons';

interface DetailsComponentProps {
    taskInstance: any;
    user: any;
}

function DetailsComponent(props: DetailsComponentProps): JSX.Element {
    const { taskInstance } = props;
    const { id } = taskInstance;

    return (
        <Row className='cvat-task-top-bar' type='flex' justify='space-between' align='middle'>
            <Col>
                <Text className='cvat-title'>{`Task details #${id}`}</Text>
            </Col>
            {props.user && props.user.isSuperuser ? 
            (<Col>
                <Dropdown overlay={
                    (
                        <ActionsMenuContainer
                            taskInstance={taskInstance}
                        />
                    )}
                >
                    <Button size='large'>
                        <Text className='cvat-text-color'>Actions</Text>
                        <Icon className='cvat-menu-icon' component={MenuIcon} />
                    </Button>
                </Dropdown>
            </Col>) : null }
        </Row>
    );
}

function mapStateToProps(state: CombinedState): any {
    const { auth } = state;
    return {
      user: auth.user
    };
  }
  
export default connect(mapStateToProps, null)(DetailsComponent);
  